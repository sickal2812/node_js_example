var express = require('express');
var router = express.Router();
const APIS = require('../apis');

router.get('/', APIS.baseAPI);
router.get('/test', APIS.testAPI);
router.post('/post_test', APIS.postAPI);

router.post('/event', APIS.event);
router.post('/gps', APIS.gps);

module.exports = router;
