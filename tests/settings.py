HELPER_SETTINGS = {
    'INSTALLED_APPS': [
        'djangocms_versioning',
        'djangocms_contentexpiry',
        'djangocms_contentexpiry.test_utils.app_1',
        'djangocms_contentexpiry.test_utils.app_2',
    ]
}


def run():
    from djangocms_helper import runner
    runner.cms('djangocms_contentexpiry', extra_args=[])


if __name__ == '__main__':
    run()
