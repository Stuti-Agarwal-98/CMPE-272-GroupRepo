const { isContext } = require("vm");
const connection = require("./connection");

module.exports.findAll = (event,contect,callback) => {
    isContext.callbackWaitsForEmptyEventLoop = false

    const sql = "SELECT * FROM curso"

    connection.query(sql, (error,rows) => {
        if (error) {
            callback({
                statusCode:500,
                body:JSON.stringify(error)
            })
        } else {
            callback(null, {
                statusCode:200,
                body:JSON.stringify({
                    todos:rows
                })
            })
        }
    })
};