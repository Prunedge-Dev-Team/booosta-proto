Step 1: Install dependencies

```shell
    pip install -r requirements.txt
```

```shell
    cd booosta_proto
    py -m grpc_tools.protoc --proto_path=./proto --python_out=./py_grpc --pyi_out=./py_grpc --grpc_python_out=./py_grpc ./proto/user.proto
```
