#!/bin/bash
aerich upgrade;
exec uvicorn smit_test.app:app --host 0.0.0.0
