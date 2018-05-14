
	let axios = require('axios');
	let cheerio = require('cheerio');
	let fs = require('fs');

	axios.get('http://www.math.purdue.edu/~li2285/courses/453f/ma453.html')
	    .then((response) => {
	        if(response.status === 200) {
	        const html = response.data;
	        console.log(cheerio.load(response.data).text());
	            const $ = cheerio.load(html); 
	    }
	    }, (error) => console.log(err) );