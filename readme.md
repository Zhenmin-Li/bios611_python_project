# Sentiment Analysis of Trump's Tweets with API

First you have to fill your API key in the "key.csv", in the space numbered 1-4
If you don't have one, see here <https://developer.twitter.com/en/apply-for-access> 

To run the environment (replace your_password with your password):

```
docker build . -t l16 --build-arg linux_user_pwd=your_password
docker run -v `pwd`:/home/rstudio -e PASSWORD=$SECRET_PWD -it l16 sudo -H -u rstudio /bin/bash -c "cd ~/; /bin/bash"
```

Then you can directly run the make file

```
make
```

Or generate the reports
```
make report.pdf
```

