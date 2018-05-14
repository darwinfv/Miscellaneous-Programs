
	const rp = require('request-promise');
	const cheerio = require('cheerio');

	const options = {
	  uri: `http://www.math.purdue.edu/~li2285/courses/453f/ma453.html`,
	  transform: function (body) {
	    return cheerio.load(body);
	  }
	};

	rp(options)
	  .then(($('html')).html() => {
	    console.log($);
	  })
	  .catch((err) => {
	    console.log("Error");
	  });

