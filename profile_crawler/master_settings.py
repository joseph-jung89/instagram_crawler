def master_settings():
    return {
        'LOG_FORMATTER': 'lib.log_formatters.PoliteLogFormatter'
        'LOG_LEVEL': 'INFO'
        'ITEM_PROCESSOR': 'lib.spawning_item_pipeline_manager.SpawningItemPipelineManager'
        'TEMP_DIRECTORY': '/tmp'
        'DEPTH_STATS': False,
        'DOWNLOAD_DELAY': 0.5,
        'CONCURRENT_REQUESTS': 1,
        'DOWNLOADER_MIDDLEWARES': {
            'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None
        }
    }

def profile_scraper_settings():
    profile_scraper_settings = {}
    profile_scraper_settings.update(master_settings())
    return profile_scraper_settings