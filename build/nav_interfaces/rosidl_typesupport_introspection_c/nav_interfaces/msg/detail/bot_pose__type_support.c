// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from nav_interfaces:msg/BotPose.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "nav_interfaces/msg/detail/bot_pose__rosidl_typesupport_introspection_c.h"
#include "nav_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "nav_interfaces/msg/detail/bot_pose__functions.h"
#include "nav_interfaces/msg/detail/bot_pose__struct.h"


// Include directives for member types
// Member `facing_direction`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void nav_interfaces__msg__BotPose__rosidl_typesupport_introspection_c__BotPose_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  nav_interfaces__msg__BotPose__init(message_memory);
}

void nav_interfaces__msg__BotPose__rosidl_typesupport_introspection_c__BotPose_fini_function(void * message_memory)
{
  nav_interfaces__msg__BotPose__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember nav_interfaces__msg__BotPose__rosidl_typesupport_introspection_c__BotPose_message_member_array[3] = {
  {
    "x",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(nav_interfaces__msg__BotPose, x),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "y",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(nav_interfaces__msg__BotPose, y),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "facing_direction",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(nav_interfaces__msg__BotPose, facing_direction),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers nav_interfaces__msg__BotPose__rosidl_typesupport_introspection_c__BotPose_message_members = {
  "nav_interfaces__msg",  // message namespace
  "BotPose",  // message name
  3,  // number of fields
  sizeof(nav_interfaces__msg__BotPose),
  nav_interfaces__msg__BotPose__rosidl_typesupport_introspection_c__BotPose_message_member_array,  // message members
  nav_interfaces__msg__BotPose__rosidl_typesupport_introspection_c__BotPose_init_function,  // function to initialize message memory (memory has to be allocated)
  nav_interfaces__msg__BotPose__rosidl_typesupport_introspection_c__BotPose_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t nav_interfaces__msg__BotPose__rosidl_typesupport_introspection_c__BotPose_message_type_support_handle = {
  0,
  &nav_interfaces__msg__BotPose__rosidl_typesupport_introspection_c__BotPose_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_nav_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, nav_interfaces, msg, BotPose)() {
  if (!nav_interfaces__msg__BotPose__rosidl_typesupport_introspection_c__BotPose_message_type_support_handle.typesupport_identifier) {
    nav_interfaces__msg__BotPose__rosidl_typesupport_introspection_c__BotPose_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &nav_interfaces__msg__BotPose__rosidl_typesupport_introspection_c__BotPose_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
