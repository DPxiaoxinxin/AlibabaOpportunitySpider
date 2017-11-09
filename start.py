from scrapy import cmdline


print("[Spider] running...")

cmdline.execute("scrapy crawl alibaba".split())

print("[Spider] done")
