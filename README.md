# Django-realfavicongenerator

Simple favicons for Dajngo! And no messin.
  
Get all devices covered, using the awesoem generator at 
http://realfavicongenerator.net/ (hence the name).

Or don't! it's completely optional. You perfectly can use this for only 
`favicon.ico` and nothing else. If you change your mind, it is a no-brainer to
add more of those fancy mobile formats.


## Installation

  *  ~~`$ pip install django-realfavicongenerator`~~ (comming soon...)  
     Instead: just copy `realfavicongenerator` directory somewhere in your 
     project (i.e. somewhere on PYTHONPATH)
  * Add `'realfavicongenerator'` to `INSTALLED_APPS`.
  * Add `url('', include('realfavicongenerator.urls')),` to `urls.py`

You are done. Of course, there are no favicons yet, we need to add them. 
Keep reading...


## Usage

First, we need to generate all those favicons and related HTML. I really like 
http://realfavicongenerator.net/ but you can use any other generator (or do 
it manually if you're... so inclined.

Three things need to be done:

### 1. 

Put all favicon files in static files in `realfavicongenerator` directory.
This includes things like `manifest.json` too.
 
There is usually one app that is "in charge" of the HTML rendering. In its
`static` directory, create new `realfavicongenerator` directory and pul all 
your favicon files there. 


### 2. 

Crate a template `realfavicongenerator/favicon.html` and paste your HTML markup 
there.

### 3.

Include the template from previous step in your `base.html`:

    {% include "realfavicongenerator/favicon.html" %}
    
Somewhere before `</head>`. Don't put it too high up, SEO evaluators might not 
like that (they like to see `<title>` quickly). 


### 4.
 
Run `$ ./manage.py collectstatic`

Required, even if `DEBUG = True`. 


## How it works?

If adds one URL pattern for each file in `static/realfavicongenerator`
directory.

For details, look in `realfavicongenerator/urls.py`.
There is nothing more to it.


## This repository

... contains a demo project. It ~~is~~ will be also used to build PyPI package.


## Dependencies

None

Tested with Django 1.9 and Python 2.7.

It is so dead simple that I expect it to work across the ages past and future.


## Contributing

Open a ticket and / or send a pull request. I don't bite. Usually.
 

## History

* initial release


## Credits

frnhr


## License

You can do whatchya want. I make no guarantees. 

If you're using this, I would love a note. Not required though.
 
For legal code, please see UNLICENSE file. 
