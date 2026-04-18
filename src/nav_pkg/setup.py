from setuptools import setup

package_name = 'nav_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/msg', ['msg/BotPose.msg']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='user@todo.todo',
    description='Dead Reckoning System',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            'commander = nav_pkg.commander:main',
            'navigator = nav_pkg.navigator:main',
        ],
    },
)
