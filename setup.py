from setuptools import dist, find_packages, setup

# `Cython` is used when installing `kss` library.
dist.Distribution().fetch_build_eggs(["Cython"])

setup(
    name="cant-revan",
    version="5.0.0",
    author="yeorinhieut",
    author_email="yeorinhieut@gmail.com",
    description="Simple Naver News Crawler",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    keywords=["naver", "news", "dataset", "nlp"],
    url="https://github.com/yeorinhieut/cant-revan",
    license="Apache-2.0",
    package_dir={"": "src"},
    packages=find_packages("src"),
    python_requires=">=3.6.0",
    install_requires=["tqdm>=4.46.0", "bs4", "lxml>=4.5.1", "aiohttp"],
    entry_points={"console_scripts": ["canrevan = canrevan:_main"]},
    classifiers=[
        "Environment :: Console",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
