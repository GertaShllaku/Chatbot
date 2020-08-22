#!/usr/bin/env python

from setuptools import setup

version = __import__('chatbot').__version__

setup(
    name='chatbotAI',
    version=version,
    description="A chatbot AI engine is a chatbot builder platform that provids both bot intelligence and"
                " chat handler with minimal codding",
    packages=['chatbot', 'chatbot.spellcheck', 'chatbot.substitution'],
    license='MIT',
    keywords='chatbot ai engine and chat builder platform',
    platforms=["Windows", "Linux", "Solaris", "Mac OS-X", "Unix"],
    package_dir={
        'chatbot': 'chatbot',
        'chatbot.spellcheck': 'chatbot/spellcheck',
        'chatbot.substitution': 'chatbot/substitution'
    },
    include_package_data=True,
    package_data={"chatbot":  ["local/en/default.template",
                               "local/en/words.txt",
                               "local/en/substitutions.json",
                               "local/pt-br/default.template"]},
    install_requires=[
          'requests',
      ]
)
