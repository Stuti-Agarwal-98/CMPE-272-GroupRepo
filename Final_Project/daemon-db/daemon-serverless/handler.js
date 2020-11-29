const db = require('./db_connect');
'use strict';


module.exports.getAllTodos = (event, context, callback) => {
  context.callbackWaitsForEmptyEventLoop = false;
  db.getAll('project_requirements')
    .then(res => {
      callback(null, {
        statusCode: 200,
        body: JSON.stringify(res)
      })
    })
    .catch(e => {
      console.log(e);
      callback(null, {
        statusCode: e.statusCode || 500,
        body: 'Error: Could not find Todos: ' + e
      })
    })
};

module.exports.createTodo = (event, context, callback) => {
  context.callbackWaitsForEmptyEventLoop = false;
  const data = JSON.parse(event.body);
  db.insert('project_requirements', data)
    .then(res => {
      callback(null,{
        statusCode: 200,
        body: "Todo Created!" + res
      })
    })
    .catch(e => {
      callback(null,{
        statusCode: e.statusCode || 500,
        body: "Could not create Todo " + e
      })
    })
};

module.exports.updateTodo = (event, context, callback) => {
  context.callbackWaitsForEmptyEventLoop = false;
  const data = JSON.parse(event.body);
  db.updateById('project_requirements', event.pathParameters.id, data)
    .then(res => {
      callback(null,{
        statusCode: 200,
        body: "Todo Updated!" + res
      })
    })
    .catch(e => {
      callback(null,{
        statusCode: e.statusCode || 500,
        body: "Could not update Todo" + e
      })
    }) 
};



