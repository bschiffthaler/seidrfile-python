#!/bin/bash
set -e -u -x

function repair_wheel {
    wheel="$1"
    if ! auditwheel show "$wheel"; then
        echo "Skipping non-platform wheel $wheel"
    else
        auditwheel repair "$wheel" --plat "$PLAT" -w /io/SeidrFile/wheelhouse/
    fi
}

# Compile wheels
for PYBIN in /opt/python/cp3{6,7,8}*/bin; do
    "${PYBIN}/pip" wheel /io/SeidrFile/ --no-deps -w wheelhouse/
done

if [ $PLAT = "manylinux2010_x86_64" ]; then
  /opt/python/cp39-cp39/bin/pip wheel /io/SeidrFile/ --no-deps -w wheelhouse/
fi
# Bundle external shared libraries into the wheels
for whl in wheelhouse/*.whl; do
    repair_wheel "$whl"
done

# Install packages and test
for PYBIN in /opt/python/cp3{6,7,8}*/bin/; do
    "${PYBIN}/pip" install SeidrFile --no-index -f /io/SeidrFile/wheelhouse/
done
if [ $PLAT = "manylinux2010_x86_64" ]; then
  /opt/python/cp39-cp39/bin/pip install SeidrFile --no-index -f /io/SeidrFile/wheelhouse/
fi