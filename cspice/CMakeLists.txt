project( CSPICE C )
file( GLOB cspice_SOURCES "./src/cspice/*.c" "./include/*.h" )
add_library( cspice SHARED ${cspice_SOURCES} )
set_target_properties( cspice PROPERTIES LINKER_LANGUAGE C )
set_target_properties( cspice PROPERTIES
    ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/lib"
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/lib"
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/bin"
)

