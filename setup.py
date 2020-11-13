
from distutils.core import setup
setup(
  name = 'Topsis_k.likhita_101803143',         # How you named your package folder (MyLib)
  packages = ['Topsis_k.likhita_101803143'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Topsis implementation as a part of coursework of ucs633 course at thapar university',   # Give a short description about your library
  author = 'K Likhita',                   # Type in your name
  author_email = 'karanamlikhita2000@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/likhita-karanam/Topsis_K.Likhita_101803143.git',   # Provide either the link to your github or to your wekeywords = ['Topsis', 'Order Preference Similarity to Ideal Solutions', ' Rank','UCS633'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'numpy',
          'pandas','sys'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
