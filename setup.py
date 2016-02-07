import os

from setuptools import setup


def readme():
    with open("README.md") as f:
        return f.read()

module_name = "pelican_resume"
module = __import__(module_name)

version = module.__version__
url = "https://github.com/cmenguy/pelican-resume"
download_url = os.path.join(url, "archive/{}.zip".format(version))

setup(name=module.__title__,
      version=module.__version__,
      description="Easily generate customizable PDF resumes from Pelican pages",
      long_description=readme(),
      url=url,
      download_url=download_url,
      author=module.__author__,
      author_email=module.__email__,
      maintainer=module.__maintainer__,
      maintainer_email=module.__email__,
      license=module.__license__,
      include_package_data=True,
      packages=[module_name],
      package_dir={module_name: module_name},
      package_data={module_name: ["static/css/*"]},
      install_requires=["pelican"],
      keywords="pelican markdown blog resume pdf",
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Topic :: Internet :: WWW/HTTP',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Text Processing',
      ],
      zip_safe=False,
      )