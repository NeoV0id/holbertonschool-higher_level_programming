#!/usr/bin/node

let logMeCount = 0;
exports.logMe = function (item) {
  console.log(logMeCount + ': ' + item);
  logMeCount += 1;
};
