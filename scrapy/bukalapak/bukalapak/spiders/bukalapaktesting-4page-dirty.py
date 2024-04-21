import scrapy

class BukalapaktestingSpider(scrapy.Spider):
    name = "bukalapaktesting"
    allowed_domains = ["bukalapak.com"]
    start_urls = ["https://www.bukalapak.com/products?page=1&search[keywords]=keyboard%20keycaps"]
    item_count = 0

    def start_requests(self):
        # Menghasilkan permintaan untuk setiap halaman dari 1 hingga 4
        for page_number in range(1, 5):
            url = f"https://www.bukalapak.com/products?page={page_number}&search[keywords]=keyboard%20keycaps"
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # Mendapatkan link untuk setiap produk
        product_links = response.css('div.bl-flex-container div.bl-flex-item div.te-product-card a::attr(href)').getall()
        
        # Melakukan iterasi untuk setiap link produk dan memanggil parse_product untuk masing-masingnya
        for product_link in product_links:
            yield scrapy.Request(url=response.urljoin(product_link), callback=self.parse_product)

    def parse_product(self, response):
        # Mendapatkan informasi yang diinginkan dari setiap produk
        title = response.css('div.c-main-product__head--left h1.c-main-product__title::text').get()
        reviews = response.css('div.c-main-product__head--left div.c-main-product__reviews div.c-main-product__rating::text').get()
        sold = response.css('div.c-main-product__head--left div.c-main-product__reviews span::text').get()
        original_price = response.css('div.bl-flex-container div.bl-flex-item div.c-main-product__price div.c-product-price span::text').get()
        store_name = response.css('a.c-link--primary--black::text').get()
        store_city = response.css('a.c-seller__city::text').get()
        description = response.css('div.c-product-details-section__main div.c-information__description-txt').xpath('string()').get()
        if description:
            # Menghilangkan semicolon dari deskripsi jika ada
            description = description.replace(';', '')
        order_processing = response.css('div.c-seller__meta__pesanan h3::text').get()
        positive_feedback = response.css('a.c-seller__meta__feedback-url::text').get()
        total_feedback = response.css('p.c-seller__meta__feedback-total::text').get()

        # Mendapatkan URL produk
        product_url = response.url

        # # Print informasi produk
        # print("Title:", title)
        # print("Reviews:", reviews)
        # print("Sold:", sold)
        # print("Original Price:", original_price)
        # print("Store Name:", store_name)
        # print("Store City:", store_city)
        # print("Description:", description)
        # print("Order Processing:", order_processing)
        # print("Positive Feedback:", positive_feedback)
        # print("Total Feedback:", total_feedback)
        # print("Product URL:", product_url)
        # print("\n")

        # Menghitung jumlah item yang diekstraksi
        self.item_count += 1

        # Yield item
        yield {
            'Title': title,
            'Reviews': reviews,
            'Sold': sold,
            'Original Price': original_price,
            'Store Name': store_name,
            'Store City': store_city,
            'Description': description,
            'Order Processing': order_processing,
            'Positive Feedback': positive_feedback,
            'Total Feedback': total_feedback,
            'Product URL': product_url
        }

    def closed(self, reason):
        # Menampilkan jumlah item yang berhasil diekstraksi setelah spider ditutup
        print("Total Items Extracted:", self.item_count)
