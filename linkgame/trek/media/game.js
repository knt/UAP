function userWins(p) {
	//Add points to the user profile
	$.ajax({
		url:'addpoints/' + p,
		type: 'post',
        async: true,
        success: function(data, status, x) {
			console.log("Good");
		},
        error: function() {
        	console.log("Bad");
        
        }
        
    });

}



function claim(concept1, relation, concept2) {
	$.ajax({
		url:'claim/' + '?c1=' + concept1 + '&c2=' + concept2 + '&relation=' + relation,
		type: 'get',
        async: true,
        success: function(data, status, x) {
			console.log("Good");
		},
        error: function() {
        	console.log("Bad");
        
        }
        
    });
    
    return false;

}