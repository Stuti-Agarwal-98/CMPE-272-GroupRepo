const mysql = require("mysql")

const rds = {
    host: "daemon-deco.caylqwlmlyc5.us-east-2.rds.amazonaws.com",
    port: "3306",
    user: "root",
    password: "root2020",
    database: "DaemonTest",
    debug: true,
}

function initializeConnection(config) {
    function Disconnect (connection) {
        connection.on("err", err => {
            if(err instanceof Error) {
                if(err.code === "PROTOCOL_CONNECTION_LOST") {
                    console.log(err.stack)
                    console.log("Lost connection. Reconnnection...")
                    initializeConnection(connection.config)                
                } else if (err.fatal) {
                  throw err
                }
            }
        })
    }

    var connection = mysql.createConnection(config)

    Disconnect(connection)

    connection.connect()
    return connection
};

const connection = initializeConnection(rds)

module.exports = connection