let express = require('express');
let bodyParser = require('body-parser');
const { json } = require('body-parser');

const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended:false}));

app.get("/",(req,res)=>{
    res.send("welcome to Bizy web app ")
})
app.post("/uploadedData",(req,res)=>{
    let array = req.body;

    console.log("Data which was sent is the following \n"+JSON.stringify(array));

    // return json({result: "this went ssuccessfull"})
    res.send("hello from server")
});

app.listen(5000);

