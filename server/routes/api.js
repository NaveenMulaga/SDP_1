const express = require('express')
const router = express.Router()

const mongoose = require('mongoose')
const db = "mongodb://localhost:27017/projectdb"

mongoose.connect(db, err => {
    if (err) {
        console.error('Érror!' +err)
    } else {
        console.log('Connected to mongodb')
    }
})
router.get('/',(_req, res) => {
    res.send('From API Route')
})

module.exports = router