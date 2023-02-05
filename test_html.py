from SESEmailer import SESEmailer

reports = {
    "status": "ok",
    "totalResults": 35,
    "articles": [
      {
        "source": {
          "id": "the-washington-post",
          "name": "The Washington Post"
        },
        "author": "Isaac Arnsdorf",
        "title": "Koch network to oppose Trump in primary after sitting out recent cycles - The Washington Post",
        "description": "The return of one of the biggest spenders in U.S. politics to the presidential primary field poses a direct challenge to the former president’s comeback bid.",
        "url": "https://www.washingtonpost.com/politics/2023/02/05/koch-trump-2024-gop-presidential-primary/",
        "urlToImage": "https://www.washingtonpost.com/wp-apps/imrs.php?src=https://arc-anglerfish-washpost-prod-washpost.s3.amazonaws.com/public/P4KHIJW2PAI6XDEHVVXSPEMMPA.jpg&w=1440",
        "publishedAt": "2023-02-05T14:22:29Z",
        "content": "Comment on this story\r\nThe network of donors and activist groups led by conservative billionaire Charles Koch will oppose Donald Trump for the 2024 Republican nomination, mounting a direct challenge … [+4978 chars]"
      },
      {
        "source": {
          "id": None,
          "name": "Fox Business"
        },
        "author": "Anders Hagstrom",
        "title": "Officials investigating Austin airport after planes nearly collide on runway - Fox Business",
        "description": "A Southwest Airlines plane nearly collided with a FedEx cargo plane at the airport in Austin, Texas on Saturday. The FAA and NTSB have opened investigations into the incident.",
        "url": "https://www.foxbusiness.com/industrials/officials-investigating-austin-airport-planes-nearly-collide-runway",
        "urlToImage": "https://a57.foxnews.com/static.foxbusiness.com/foxbusiness.com/content/uploads/2023/01/0/0/FAA-Outage-Southwest-Flights-Delays-Cancellations.jpg?ve=1&tl=1",
        "publishedAt": "2023-02-05T12:40:52Z",
        "content": "U.S. aviation officials have opened an investigation at the Austin, Texas, airport after two planes operated by FedEx and Southwest Airlines could have collided Saturday.\r\nThe incident occurred when … [+1823 chars]"
      },
      {
        "source": {
          "id": "cbs-news",
          "name": "CBS News"
        },
        "author": None,
        "title": "Suspected Chinese spy balloon shot down off South Carolina coast - CBS News",
        "description": "Secretary of Defense Lloyd Austin said President Biden authorized the operation to shoot down the balloon.",
        "url": "https://www.cbsnews.com/news/chinese-spy-balloon-shot-down-off-carolina-coast/",
        "urlToImage": "https://assets3.cbsnewsstatic.com/hub/i/r/2023/02/04/021dbc7a-e5e8-46ba-a3ca-475181cc201d/thumbnail/1200x630/fe033aabcd3e07ec7ecbd49d27f84866/ap23035604212451.jpg",
        "publishedAt": "2023-02-05T12:23:00Z",
        "content": "The suspected Chinese spy balloon that has been drifting across the United States for several days has been shot down off the coast of South Carolina.\r\nThe balloon was shot down by U.S. fighter jets … [+6336 chars]"
      },
    ]
}

emailer = SESEmailer(
    "Charlie <news@charliebushman.com>",
    "ctbushman@gmail.com",
    "ConfigSet",
    "us-east-1",
)

emailer.send_email(reports, True)