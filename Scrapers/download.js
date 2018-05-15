	
	const fs = require('fs');
	const download = require('download');
	 
	download('http://www.math.purdue.edu/~li2285/courses/453f/quiz2_sol.pdf', 'dist').then(() => {
	    console.log('done!');
	});
	 
	Promise.all([].map(x => download(x, 'dist'))).then(() => {
	    console.log('files downloaded!');
	});