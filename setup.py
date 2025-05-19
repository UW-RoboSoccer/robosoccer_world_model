from setuptools import setup

package_name = 'world_model'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'rclpy', 'geometry_msgs', 'std_msgs'],
    zip_safe=True,
    maintainer='UWRS',
    maintainer_email='uwrobosoccer@gmail.com',
    description='World model node for RoboSoccer',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'world_model_node = world_model.world_model_node:main',
        ],
    },
)
