
function baseAPI (req,res) {
    res.status(200).json(
        {
            "success" : true
        }
    );
}

function testAPI (req,res) {
    res.status(200).json(
        {
            "success" : true
        }
    );
}

function postAPI (req,res) {
    const custom_message = req.body.message;
    res.status(200).json(
        {
            "success" : custom_message
        }
    );
}

function gps (req,res) {
    if(req.body.event == true && req.body.key == 'bfff93158293e54c7689f8b326419f83633f3f4b') {
        res.status(200).json(
            {
                "status" : "success",
                "key" : req.body.key
            }
        );
    } else {
        res.status(200).json(
            {
                "status" : "fail"
            }
        )
    };
}

function event (req,res) {
    const custom_message = req.body.message;

    res.status(200).json(
        {
            "success" : custom_message
        }
    );
}

module.exports = {
    baseAPI : baseAPI,
    testAPI : testAPI,
    postAPI : postAPI,
    gps : gps,
    event : event,
}