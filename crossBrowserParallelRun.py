from multiprocessing.pool import ThreadPool
from browserstack_webAutomation_accesskeys import run_test

devices = [
    {
        'browserName': 'Chrome',
        'os': 'Windows',
        'os_version': '11',
        'name': 'Windows Chrome'
    },
    {
        'browserName': 'Firefox',
        'os': 'OS X',
        'os_version': 'Monterey',
        'name': 'Mac Firefox'
    },
    {
        'device': 'iPhone 13',
        'real_mobile': 'true',
        'os_version': '15',
        'browserName': 'Safari',
        'name': 'iPhone Safari'
    },
    {
        'device': 'Samsung Galaxy S21',
        'real_mobile': 'true',
        'os_version': '11.0',
        'browserName': 'Chrome',
        'name': 'Samsung Chrome'
    },
    {
        'browserName': 'Edge',
        'os': 'Windows',
        'os_version': '10',
        'name': 'Windows Edge'
    }
]

if __name__ == '__main__':
    pool = ThreadPool(processes=5)
    pool.map(run_test, devices)
