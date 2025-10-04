# Hamilton STAR Firmware Command Reference

This document provides a comprehensive reference of Hamilton STAR firmware commands used in the PyLabRobot library. The commands are organized by module with detailed explanations of what each command does, its parameters, and where it is implemented in the codebase.

## Module C0 (Controller/Master)

| Command | Function Name | Description | Parameters | Implementation (Line) |
|---------|---------------|-------------|------------|------------------------|
| VI | pre_initialize_instrument | Pre-initialize instrument | None | STAR_backend.py:3269 |
| RE | request_error_code | Request error code - retrieves last saved error messages | None | STAR_backend.py:3324 |
| RF | request_firmware_version | Request firmware version information | None | STAR_backend.py:3332 |
| RA | request_parameter_value | Request parameter value from the instrument | None | STAR_backend.py:3340 |
| QB | request_electronic_board_type | Request electronic board type (C167CR, LPC2468, etc.) | None | STAR_backend.py:3356 |
| MU | request_supply_voltage | Request supply voltage (for LDPB only) | None | STAR_backend.py:3369 |
| QW | request_instrument_initialization_status | Request instrument initialization status | None | STAR_backend.py:3374 |
| VP | request_name_of_last_faulty_parameter | Request name of last faulty parameter | None | STAR_backend.py:3394 |
| RQ | request_master_status | Request master status | None | STAR_backend.py:3402 |
| SR | request_number_of_presence_sensors_installed | Request number of presence sensors installed | None | STAR_backend.py:3411 |
| QV | request_eeprom_data_correctness | Request EEPROM data correctness | None | STAR_backend.py:3420 |
| NS | trigger_next_step | Trigger next step (Single step mode) | None | STAR_backend.py:3443 |
| HD | halt | Halt ongoing operations immediately | None | STAR_backend.py:3453 |
| AZ | save_all_cycle_counters | Save all cycle counters of the instrument | None | STAR_backend.py:3461 |
| AB | set_not_stop | Set non-stop mode ON | None | STAR_backend.py:3472 |
| AW | set_not_stop | Set non-stop mode OFF | None | STAR_backend.py:3474 |
| SI | store_installation_data | Store installation date and serial number | serial_number, installation_date | STAR_backend.py:3491 |
| AT | additional_time_stamp | Add additional timestamp | year, month, day, hour, minute, second | STAR_backend.py:3520 |
| AG | set_x_offset_x_axis_iswap | Set X-offset between X-axis and iSWAP | x_offset | STAR_backend.py:3529 |
| AF | set_x_offset_x_axis_core_96_head | Set X-offset between X-axis and CoRe 96 head | x_offset | STAR_backend.py:3538 |
| RT | request_tip_presence | Request query tip presence on each channel | None | STAR_backend.py:5143 |
| RL | request_pip_height_last_lld | Request PIP height of last LLD (Liquid Level Detection) | None | STAR_backend.py:5153 |
| QS | request_tadm_status | Request TADM status (0=off, 1=on) | None | STAR_backend.py:5162 |
| EV | move_core_96_to_safe_position | Move CoRe 96 Head to Z save position | None | STAR_backend.py:5323 |
| QH | request_tip_presence_in_core_96_head | Request tip presence in CoRe 96 Head | None | STAR_backend.py:5897 |
| QI | request_position_of_core_96_head | Request position of CoRe 96 Head | None | STAR_backend.py:5909 |
| VC | request_core_96_head_channel_tadm_status | Request CoRe 96 Head channel TADM Status | None | STAR_backend.py:5922 |
| VB | request_core_96_head_channel_tadm_error_status | Request CoRe 96 Head channel TADM error status | None | STAR_backend.py:5931 |
| ZO | core_open_gripper | Open CoRe gripper tool | None | STAR_backend.py:4809 |
| JE | spread_pip_channels | Spread PIP channels to specified positions | channel_pattern, x_positions | STAR_backend.py:5015 |
| ZA | move_all_channels_in_z_safety | Move all pipetting channels to Z-safety position | None | STAR_backend.py:5081 |
| AS | aspirate_pip | Aspiration of liquid using PIP | tip_pattern, volumes, speeds, etc. | STAR_backend.py:4462 |
| DS | dispense_pip | Dispensing of liquid using PIP | tip_pattern, volumes, speeds, etc. | STAR_backend.py:4696 |
| EI | initialize_core_96_head | Initialize CoRe 96 Head | None | STAR_backend.py:5311 |
| PI | put_in_hotel | Put plate in a storage location | location, heights, etc. | STAR_backend.py:7856 |
| PO | get_from_hotel | Get plate from a storage location | location, heights, etc. | STAR_backend.py:7930 |

## Module R0 (iSWAP Robotic Arm)

| Command | Function Name | Description | Parameters | Implementation (Line) |
|---------|---------------|-------------|------------|------------------------|
| BA | iswap_dangerous_release_break | Release iSWAP brake (dangerous operation) | None | STAR_backend.py:6802 |
| BO | iswap_reengage_break | Re-engage iSWAP brake | None | STAR_backend.py:6805 |
| ZI | iswap_initialize_z_axis | Initialize iSWAP Z-axis | None | STAR_backend.py:6808 |
| QW | request_iswap_initialization_status | Request iSWAP initialization status | None | STAR_backend.py:7091 |
| WP | position_iswap_with_plate | Position iSWAP with plate | x_position, y_position, z_position, etc. | STAR_backend.py:7463 |
| TP | position_iswap_transport_position | Position iSWAP in transport position | minimum_height, etc. | STAR_backend.py:7477 |
| RP | request_iswap_position | Request iSWAP current position | None | STAR_backend.py:7083 |
| RR | rotate_iswap | Rotate iSWAP to specified position | angle, speed, etc. | STAR_backend.py:6745 |
| GP | iswap_get_plate | iSWAP grab plate from specified position | x_position, y_position, grip_strength, etc. | STAR_backend.py:6561 |
| PP | iswap_put_plate | iSWAP put plate at specified position | x_position, y_position, etc. | STAR_backend.py:6658 |
| OG | iswap_open_gripper | Open iSWAP gripper | open_position | STAR_backend.py:6491 |
| CG | iswap_close_gripper | Close iSWAP gripper | close_position, grip_strength, etc. | STAR_backend.py:6507 |

## Module I0 (X-drive/Autoload)

| Command | Function Name | Description | Parameters | Implementation (Line) |
|---------|---------------|-------------|------------|------------------------|
| QW | request_autoload_initialization_status | Request autoload initialization status | None | STAR_backend.py:3380 |
| XP | move_autoload_to_slot | Position autoload to a specific slot/track | slot_number | STAR_backend.py:6030 |
| XP | park_autoload | Park autoload to maximum X position | None | STAR_backend.py:6040 |
| CA | push_out_carrier_to_loading_tray | Push out carrier to loading tray (after identification) | Not implemented yet (TODO in code) | - |

## Module H0 (Heater/Shaker)

| Command | Function Name | Description | Parameters | Implementation (Line) |
|---------|---------------|-------------|------------|------------------------|
| QW | request_core_96_head_initialization_status | Request CoRe 96 head initialization status | None | STAR_backend.py:5327 |

## Channel Modules (P1-PG)

The Hamilton STAR has individual addressable pipetting channels, referred to by module IDs P1 through PG (P1, P2, P3, P4, P5, P6, P7, P8, P9, PA, PB, PC, PD, PE, PF, PG). These correspond to channels 0-15 in PyLabRobot.

| Command | Function Name | Description | Parameters | Implementation (Line) |
|---------|---------------|-------------|------------|------------------------|
| SI | violently_shoot_down_tip | Emergency tip ejection - shoots tip down at high acceleration (considered an "easter egg" in the code) | None | STAR_backend.py:7967 |

## Command Structure

All STAR firmware commands follow a standard structure:

1. **Module ID**: Identifies the specific hardware module (e.g., C0, R0, I0, H0, P1-PG)
2. **Command Code**: Two-letter code that identifies the specific action (e.g., VI, RE, RF)
3. **Parameters**: Optional parameters passed to the command (formatted based on command requirements)

The PyLabRobot implementation uses the `send_command` method to communicate with the Hamilton STAR firmware, where commands are sent in the format: `module="XX", command="YY", [parameters]`
