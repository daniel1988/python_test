#!/usr/bin/env bash
root=$(cd "$(dirname "$0")"; cd ../; pwd)
gen_py_dir=$root/Thrift

if [ ! -d $gen_py_dir ]; then
    mkdir -p $gen_py_dir
fi

rm -rf $gen_py_dir/*
thrift -v -r --out $gen_py_dir --gen py:server HelloService.thrift
