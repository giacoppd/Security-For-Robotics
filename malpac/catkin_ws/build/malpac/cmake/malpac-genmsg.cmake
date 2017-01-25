# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "malpac: 1 messages, 0 services")

set(MSG_I_FLAGS "-Imalpac:/home/dominic/malpac/catkin_ws/src/malpac/msg;-Istd_msgs:/opt/ros/indigo/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(genlisp REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(malpac_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/dominic/malpac/catkin_ws/src/malpac/msg/test.msg" NAME_WE)
add_custom_target(_malpac_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "malpac" "/home/dominic/malpac/catkin_ws/src/malpac/msg/test.msg" ""
)

#
#  langs = gencpp;genlisp;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(malpac
  "/home/dominic/malpac/catkin_ws/src/malpac/msg/test.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/malpac
)

### Generating Services

### Generating Module File
_generate_module_cpp(malpac
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/malpac
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(malpac_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(malpac_generate_messages malpac_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/dominic/malpac/catkin_ws/src/malpac/msg/test.msg" NAME_WE)
add_dependencies(malpac_generate_messages_cpp _malpac_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(malpac_gencpp)
add_dependencies(malpac_gencpp malpac_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS malpac_generate_messages_cpp)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(malpac
  "/home/dominic/malpac/catkin_ws/src/malpac/msg/test.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/malpac
)

### Generating Services

### Generating Module File
_generate_module_lisp(malpac
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/malpac
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(malpac_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(malpac_generate_messages malpac_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/dominic/malpac/catkin_ws/src/malpac/msg/test.msg" NAME_WE)
add_dependencies(malpac_generate_messages_lisp _malpac_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(malpac_genlisp)
add_dependencies(malpac_genlisp malpac_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS malpac_generate_messages_lisp)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(malpac
  "/home/dominic/malpac/catkin_ws/src/malpac/msg/test.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/malpac
)

### Generating Services

### Generating Module File
_generate_module_py(malpac
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/malpac
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(malpac_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(malpac_generate_messages malpac_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/dominic/malpac/catkin_ws/src/malpac/msg/test.msg" NAME_WE)
add_dependencies(malpac_generate_messages_py _malpac_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(malpac_genpy)
add_dependencies(malpac_genpy malpac_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS malpac_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/malpac)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/malpac
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
add_dependencies(malpac_generate_messages_cpp std_msgs_generate_messages_cpp)

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/malpac)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/malpac
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
add_dependencies(malpac_generate_messages_lisp std_msgs_generate_messages_lisp)

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/malpac)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/malpac\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/malpac
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
add_dependencies(malpac_generate_messages_py std_msgs_generate_messages_py)
