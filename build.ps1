mkdir build;
pushd build;

conan install ..
conan build ..

popd;