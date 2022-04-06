#!/usr/bin/node

exports.esrever = function (list) {
  const new_list = [];
  /* new_list = new_list.toCamelCase; */
  for (let i = list.length - 1; i >= 0; i--) {
		    new_list.push(list[i]);
  }
  return new_list;
};
