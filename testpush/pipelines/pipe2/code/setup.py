from setuptools import setup, find_packages
setup(
    name = 'pipe2',
    version = '1.0',
    packages = find_packages(include = ('pipe2*', )) + ['prophecy_config_instances.pipe2'],
    package_dir = {'prophecy_config_instances.pipe2' : 'configs/resources/pipe2'},
    package_data = {'prophecy_config_instances.pipe2' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.9.46'],
    entry_points = {
'console_scripts' : [
'main = pipe2.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
