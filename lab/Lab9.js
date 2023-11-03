var http = require("http"); 
var data = require("C:/Users/rcase/Documents/POWERSHELL/Node/widgets.json"); 


//Pulling all data related to color from the widget
 
function listAll(res) { 
    var colorAll = data.filter(function(item) { 
        return item.color === "blue","green","black"; 
    }); 

    res.end(JSON.stringify(colorAll)); 
} 



//converting all data into string format with no specific address

 
var server = http.createServer(function(req, res){ 
    if (req.url === "/") { 
 res.writeHead(200, {"Content-Type": "text/json"}); 
        res.end(JSON.stringify(data));
    
}

//If requesting "/All" will display information about the widget in an easy to read format

else if (req.url === "/All") { 
res.end('<p style="color: blue">Widget1 is blue</p> <p style="color: green">Widget2 is green</p> <p style="color: black">Widget3 is black</p> <p style="color: blue">Widgetx is blue</p> ')

	
//If the address is wrong it will report data not found

}else { 
        res.writeHead(404, {"Content-Type": "text/plain"});       
        res.end("Data not found");         
    } 
}); 
 





server.listen(3000); 
console.log("Server is listening on port 3000");