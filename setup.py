from distutils.core import setup

setup(
    name="twilist",
    packages=["twilist"],
    version="0.1",
    description="managing tweet draft through CLI",
    author="kecebongsoft",
    author_email="kecebongsoft@gmail.com",
    url="http://github.com/kecebongsoft/twilist",
    keywords=["tweet","twidge"],
    scripts=["scripts/twilist"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ],
    long_description="""\
    twilist
    ------------------------------------------------------------

    twilist is a CLI tool for you to manage your tweet drafts from
    command line, for full usage, see readme.md on the github repo:

    http://github.com/kecebongsoft/twilist

    """
)
