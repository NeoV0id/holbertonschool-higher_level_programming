#!/usr/bin/node

exports.esrever = function (list) {
  const new_list = [];
  new_list = new_list.toCamelCase;
  for (let j = 0; j < list.length; j++) {
    for (let i = list.length; i > 0; i--) {
      new_list[j] = list[i];
    }
  }
  return new_list;
};
