# Hamilton STAR Error Codes by Module

This document lists error codes and messages per module as implemented in `pylabrobot/liquid_handling/backends/hamilton/STAR_backend.py`. Columns: error code, English message, and Chinese translation.

Note on C0 (Master): Responses report `error_code/trace_information`. We provide two tables: master error codes (primary) and C0 trace information codes.

## Master (C0) — Primary error codes

| Code | Message | 中文翻译 |
|---:|---|---|
| 01 | Command syntax error | 命令语法错误 |
| 02 | Hardware error | 硬件错误 |
| 03 | Command not completed | 命令未完成 |
| 04 | Clot detected | 检测到凝块 |
| 05 | Barcode unreadable | 条码不可读 |
| 06 | Too little liquid | 液体量不足 |
| 07 | Tip already fitted | 吸头已装载 |
| 08 | No tips | 无吸头 |
| 09 | No carrier | 无载架 |
| 10 | Not completed | 未完成 |
| 11 | Dispense with pressure LLD | 压力LLD下禁止分液 |
| 12 | No Teach In Signal | 无校准信号 |
| 13 | Loading Tray error | 上料托盘错误 |
| 14 | Sequenced aspiration with pressure LLD | 压力LLD下不允许序列吸液 |
| 15 | Not allowed parameter combination | 参数组合不允许 |
| 16 | Cover close error | 盖子关闭错误 |
| 17 | Aspiration error | 吸液错误 |
| 18 | Wash fluid or trash error | 清洗液/废液错误 |
| 19 | Incubation error | 孵育错误 |
| 20 | TADM measurement error | TADM测量错误 |
| 21 | No element | 无元件 |
| 22 | Element still holding | 元件仍被抓取 |
| 23 | Element lost | 元件丢失 |
| 24 | Illegal target plate position | 目标板位非法 |
| 25 | Illegal user access | 非法用户操作 |
| 26 | TADM measurement error | TADM测量错误 |
| 27 | Position not reachable | 位置不可达 |
| 28 | Unexpected LLD | 意外液面检测 |
| 29 | Area already occupied | 区域已被占用 |
| 30 | Impossible to occupy area | 区域无法占用 |
| 31 | Anti drop controlling out of tolerance | 防滴控制超出允许范围 |
| 32 | Decapper lock error | 旋盖器锁定错误 |
| 33 | Decapper station error | 旋盖工位错误 |
| 99 | Slave error | 从模块错误 |
| 100 | Wrong carrier barcode detected | 载架条码错误 |
| 101 | Carrier barcode could not be read or is missing | 载架条码不可读或缺失 |
| 102 | Liquid surface not detected | 未检测到液面 |
| 103 | Carrier not detected at deck end position | 未在平台末端检测到载架 |
| 104 | Dispense volume exceeds the aspirated volume | 分液体积超过吸液体积 |
| 105 | The dispensed volume is out of tolerance | 分液体积超出公差 |
| 106 | The labware to be loaded was not detected by autoload | 自动上料未检测到耗材 |
| 107 | The labware contains unexpected barcode | 耗材条码异常 |
| 108 | The labware to be reloaded contains wrong barcode | 重新上料的耗材条码错误 |
| 109 | The barcode read doesn't match the barcode mask defined | 条码不符合定义的掩码 |
| 110 | The barcode read is not unique | 条码不唯一 |
| 111 | The barcode read is already loaded as unique barcode | 条码已作为唯一条码被加载 |
| 112 | Kit Lot expired | 试剂盒批次过期 |
| 113 | Barcode contains delimiter character | 条码包含分隔符字符 |

## Master (C0) — Trace information codes

| Code | Message | 中文翻译 |
|---:|---|---|
| 10 | CAN error | CAN错误 |
| 11 | Slave command time out | 从模块命令超时 |
| 20 | E2PROM error | E2PROM错误 |
| 30 | Unknown command | 未知命令 |
| 31 | Unknown parameter | 未知参数 |
| 32 | Parameter out of range | 参数超出范围 |
| 33 | Parameter does not belong to command, or not all parameters were sent | 参数不属于该命令，或未发送完整参数 |
| 34 | Node name unknown | 节点名称未知 |
| 35 | id parameter error | id参数错误 |
| 37 | node name defined twice | 节点名称重复定义 |
| 38 | faulty XL channel settings | XL通道设置错误 |
| 39 | faulty robotic channel settings | 机械臂通道设置错误 |
| 40 | PIP task busy | PIP任务忙 |
| 41 | Auto load task busy | 自动上料任务忙 |
| 42 | Miscellaneous task busy | 杂项任务忙 |
| 43 | Incubator task busy | 孵育任务忙 |
| 44 | Washer task busy | 清洗站任务忙 |
| 45 | iSWAP task busy | iSWAP任务忙 |
| 46 | CoRe 96 head task busy | CoRe 96头任务忙 |
| 47 | Carrier sensor doesn't work properly | 载架传感器异常 |
| 48 | CoRe 384 head task busy | CoRe 384头任务忙 |
| 49 | Nano pipettor task busy | 纳升级量器任务忙 |
| 50 | XL channel task busy | XL通道任务忙 |
| 51 | Tube gripper task busy | 试管夹任务忙 |
| 52 | Imaging channel task busy | 成像通道任务忙 |
| 53 | Robotic channel task busy | 机械臂通道任务忙 |

## Autoload (I0)

| Code | Message | 中文翻译 |
|---:|---|---|
| 36 | Hamilton will not run while the hood is open | 罩门打开时系统不会运行 |

## Pipetting channels (PX, P1–PG)

| Code | Message | 中文翻译 |
|---:|---|---|
| 0 | No error | 无错误 |
| 20 | No communication to EEPROM | 无法与EEPROM通信 |
| 30 | Unknown command | 未知命令 |
| 31 | Unknown parameter | 未知参数 |
| 32 | Parameter out of range | 参数超出范围 |
| 35 | Voltages outside permitted range | 电压超出允许范围 |
| 36 | Stop during execution of command | 命令执行过程中停止 |
| 37 | Stop during execution of command | 命令执行过程中停止 |
| 40 | No parallel processes permitted (Two or more commands sent for the same control process) | 不允许并行过程（同一控制流程收到多个命令） |
| 50 | Dispensing drive init. position not found | 分液驱动初始位置未找到 |
| 51 | Dispensing drive not initialized | 分液驱动未初始化 |
| 52 | Dispensing drive movement error | 分液驱动运动错误 |
| 53 | Maximum volume in tip reached | 吸头内体积达到上限 |
| 54 | Position outside of permitted area | 位置超出允许区域 |
| 55 | Y-drive blocked | Y轴驱动阻塞 |
| 56 | Y-drive not initialized | Y轴驱动未初始化 |
| 57 | Y-drive movement error | Y轴驱动运动错误 |
| 60 | Z-drive blocked | Z轴驱动阻塞 |
| 61 | Z-drive not initialized | Z轴驱动未初始化 |
| 62 | Z-drive movement error | Z轴驱动运动错误 |
| 63 | Z-drive limit stop not found | Z轴限位未找到 |
| 70 | No liquid level found (possibly because no liquid was present) | 未检测到液面（可能无液体） |
| 71 | Not enough liquid present | 液体不足 |
| 72 | Auto calibration at pressure (Sensor not possible) | 压力自动校准不可用（传感器） |
| 73 | No liquid level found with dual LLD | 双LLD未检测到液面 |
| 74 | Liquid at a not allowed position detected | 检测到液体处于不允许的位置 |
| 75 | No tip picked up | 未拾取到吸头 |
| 76 | Tip already picked up | 吸头已拾取 |
| 77 | Tip not droped | 吸头未丢弃 |
| 78 | Wrong tip picked up | 拾取了错误的吸头 |
| 80 | Liquid not correctly aspirated | 吸液不正确 |
| 81 | Clot detected | 检测到凝块 |
| 82 | TADM measurement out of lower limit curve | TADM测量低于下限曲线 |
| 83 | TADM measurement out of upper limit curve | TADM测量高于上限曲线 |
| 84 | Not enough memory for TADM measurement | TADM测量内存不足 |
| 85 | No communication to digital potentiometer | 无法与数字电位器通信 |
| 86 | ADC algorithm error | ADC算法错误 |
| 87 | 2nd phase of liquid not found | 第二相液体未检测到 |
| 88 | Not enough liquid present | 液体不足 |
| 90 | Limit curve not resetable | 限制曲线不可复位 |
| 91 | Limit curve not programmable | 限制曲线不可编程 |
| 92 | Limit curve not found | 限制曲线未找到 |
| 93 | Limit curve data incorrect | 限制曲线数据错误 |
| 94 | Not enough memory for limit curve | 限制曲线内存不足 |
| 95 | Invalid limit curve index | 限制曲线索引无效 |
| 96 | Limit curve already stored | 限制曲线已存储 |

## CoRe 96 head (H0)

| Code | Message | 中文翻译 |
|---:|---|---|
| 20 | No communication to EEPROM | 无法与EEPROM通信 |
| 30 | Unknown command | 未知命令 |
| 31 | Unknown parameter | 未知参数 |
| 32 | Parameter out of range | 参数超出范围 |
| 35 | Voltage outside permitted range | 电压超出允许范围 |
| 36 | Stop during execution of command | 命令执行过程中停止 |
| 37 | The adjustment sensor did not switch | 调整传感器未触发 |
| 40 | No parallel processes permitted | 不允许并行过程 |
| 50 | Dispensing drive initialization failed | 分液驱动初始化失败 |
| 51 | Dispensing drive not initialized | 分液驱动未初始化 |
| 52 | Dispensing drive movement error | 分液驱动运动错误 |
| 53 | Maximum volume in tip reached | 吸头内体积达到上限 |
| 54 | Position out of permitted area | 位置超出允许区域 |
| 55 | Y drive initialization failed | Y轴初始化失败 |
| 56 | Y drive not initialized | Y轴未初始化 |
| 57 | Y drive movement error | Y轴运动错误 |
| 58 | Y drive position outside of permitted area | Y轴位置超出允许区域 |
| 60 | Z drive initialization failed | Z轴初始化失败 |
| 61 | Z drive not initialized | Z轴未初始化 |
| 62 | Z drive movement error | Z轴运动错误 |
| 63 | Z drive position outside of permitted area | Z轴位置超出允许区域 |
| 65 | Squeezer drive initialization failed | 压夹驱动初始化失败 |
| 66 | Squeezer drive not initialized | 压夹驱动未初始化 |
| 67 | Squeezer drive movement error: drive blocked or incremental sensor fault | 压夹驱动运动错误：驱动阻塞或增量传感器故障 |
| 68 | Squeezer drive position outside of permitted area | 压夹驱动位置超出允许区域 |
| 70 | No liquid level found | 未检测到液面 |
| 71 | Not enough liquid present | 液体不足 |
| 75 | No tip picked up | 未拾取到吸头 |
| 76 | Tip already picked up | 吸头已拾取 |
| 81 | Clot detected | 检测到凝块 |

## iSWAP (R0)

| Code | Message | 中文翻译 |
|---:|---|---|
| 20 | No communication to EEPROM | 无法与EEPROM通信 |
| 30 | Unknown command | 未知命令 |
| 31 | Unknown parameter | 未知参数 |
| 32 | Parameter out of range | 参数超出范围 |
| 33 | FW doesn't match to HW | 固件与硬件不匹配 |
| 36 | Stop during execution of command | 命令执行过程中停止 |
| 37 | The adjustment sensor did not switch | 调整传感器未触发 |
| 38 | The adjustment sensor cannot be searched | 无法搜索调整传感器 |
| 40 | No parallel processes permitted | 不允许并行过程 |
| 41 | No parallel processes permitted | 不允许并行过程 |
| 42 | No parallel processes permitted | 不允许并行过程 |
| 50 | Y-drive Initialization failed | Y轴初始化失败 |
| 51 | Y-drive not initialized | Y轴未初始化 |
| 52 | Y-drive movement error: drive locked or incremental sensor fault | Y轴运动错误：驱动锁定或增量传感器故障 |
| 53 | Y-drive movement error: position counter over/underflow | Y轴运动错误：位置计数器上/下溢 |
| 60 | Z-drive initialization failed | Z轴初始化失败 |
| 61 | Z-drive not initialized | Z轴未初始化 |
| 62 | Z-drive movement error: drive locked or incremental sensor fault | Z轴运动错误：驱动锁定或增量传感器故障 |
| 63 | Z-drive movement error: position counter over/underflow | Z轴运动错误：位置计数器上/下溢 |
| 70 | Rotation-drive initialization failed | 旋转轴初始化失败 |
| 71 | Rotation-drive not initialized | 旋转轴未初始化 |
| 72 | Rotation-drive movement error: drive locked or incremental sensor fault | 旋转轴运动错误：驱动锁定或增量传感器故障 |
| 73 | Rotation-drive movement error: position counter over/underflow | 旋转轴运动错误：位置计数器上/下溢 |
| 80 | Wrist twist drive initialization failed | 手腕扭转驱动初始化失败 |
| 81 | Wrist twist drive not initialized | 手腕扭转驱动未初始化 |
| 82 | Wrist twist drive movement error: drive locked or incremental sensor fault | 手腕扭转驱动运动错误：驱动锁定或增量传感器故障 |
| 83 | Wrist twist drive movement error: position counter over/underflow | 手腕扭转驱动运动错误：位置计数器上/下溢 |
| 85 | Gripper drive: communication error to gripper DMS digital potentiometer | 夹爪驱动：与DMS数字电位器通信错误 |
| 86 | Gripper drive: Auto adjustment of DMS digital potentiometer not possible | 夹爪驱动：无法自动调整DMS数字电位器 |
| 89 | Gripper drive movement error: drive locked or incremental sensor fault during gripping | 夹爪驱动运动错误：抓取过程中驱动锁定或增量传感器故障 |
| 90 | Gripper drive initialized failed | 夹爪驱动初始化失败 |
| 91 | iSWAP not initialized. Call star.initialize_iswap(). | iSWAP未初始化。请调用 star.initialize_iswap()。 |
| 92 | Gripper drive movement error: drive locked or incremental sensor fault during release | 夹爪驱动运动错误：释放过程中驱动锁定或增量传感器故障 |
| 93 | Gripper drive movement error: position counter over/underflow | 夹爪驱动运动错误：位置计数器上/下溢 |
| 94 | Plate not found | 未找到板 |
| 96 | Plate not available | 板不可用 |
| 97 | Unexpected object found | 发现意外物体 |

---

### Coverage and gaps
- Modules with explicit tables: C0 (master + trace), I0, PX/P1–PG, H0, R0.
- Other module IDs exist (X0, W1, W2, T1, T2, HW, HU, HV, N0, D0, NP, M1), but the backend does not include trace-information tables for them; unknown codes will appear as “Unknown trace information code ##”.
