---
sidebar_position: 4
title: Instance Status
sidebar_label: Instance Status
---

The status of a compute instance refers to the various states an instance goes through from startup to release. Proper management of the instance throughout its lifecycle—from startup to termination—ensures that the applications running on the instance can efficiently provide services.

|  Status Name  |    Status Type     | Description                                                                                                                                                                                                                      |
| :-----------: | :----------------: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   Starting    | Intermediate State | The state after the instance is created or powered on from a shutdown state, but before it reaches the "Running" state.                                                                                                          |
|    Running    |    Stable State    | The instance is running normally, and you can operate your applications on it.                                                                                                                                                   |
| Shutting Down | Intermediate State | The state after the instance receives a shutdown command from the console, but before it reaches the "Shutdown" state. If it remains in this state for a long time, it may indicate an issue. Force shutdown is not recommended. |
|   Shutdown    |    Stable State    | The instance has been stopped properly and is no longer providing services. Some instance properties can only be modified in the shutdown state.                                                                                 |
|   Deleting    | Intermediate State | The state after the instance is shut down and receives a delete command from the console, but before the deletion is completed.                                                                                                  |
