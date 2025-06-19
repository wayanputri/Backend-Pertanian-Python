PROTO_DIR=proto
OUT_DIR=pb
GOOGLE_APIS=$(PROTO_DIR)/googleapis

generate: ensure-gen-dir
	python -m grpc_tools.protoc -Iproto -Iproto/googleapis --python_out=pb --grpc_python_out=pb --descriptor_set_out=pb/api.pb --include_imports --openapiv2_out=pb proto/api.proto

ensure-gen-dir:
	@if not exist $(OUT_DIR) mkdir $(OUT_DIR)

clean:
	@echo "Cleaning generated files..."
	@if exist $(OUT_DIR) rmdir /s /q $(OUT_DIR)

run-ui:
	python app_http.py
run-grpc:
	python grpc_server.py
update-requirement:
	pip freeze > requirements.txt

nenv:
	.\venv\Scripts\activate



