# User Manual

Comprehensive guide for using the Haier Liquid Handling System.

## Table of Contents

1. [Overview](#overview)
2. [User Interface](#user-interface)
3. [Protocol Management](#protocol-management)
4. [Running Protocols](#running-protocols)
5. [Data Management](#data-management)
6. [Maintenance](#maintenance)
7. [Safety Guidelines](#safety-guidelines)

## Overview

The Haier Liquid Handling System is designed for precise, automated liquid handling operations in laboratory environments. This manual covers day-to-day operations for end users.

### Key Features

- **Automated Pipetting**: Precise volume control from 1 μL to 1000 μL
- **Protocol Designer**: Visual protocol creation and editing
- **Real-time Monitoring**: Live status and progress tracking
- **Data Management**: Comprehensive result storage and analysis
- **Quality Control**: Built-in validation and error detection

## User Interface

### Main Dashboard

The main dashboard provides an overview of system status:

- **System Status**: Current state (Ready, Running, Error, Maintenance)
- **Active Protocols**: Currently running or queued protocols
- **Recent Results**: Latest completed runs
- **Alerts**: System notifications and warnings

### Navigation Menu

| Section | Description |
|---------|-------------|
| Dashboard | System overview and status |
| Protocols | Protocol management and designer |
| Results | Data viewing and analysis |
| Devices | Device status and configuration |
| Settings | User preferences and system settings |
| Help | Documentation and support |

### Toolbar Functions

Common toolbar actions:
- **New Protocol** (Ctrl+N): Create a new protocol
- **Open Protocol** (Ctrl+O): Load existing protocol
- **Save** (Ctrl+S): Save current work
- **Run** (F5): Execute selected protocol
- **Stop** (Esc): Halt current operation
- **Emergency Stop** (F12): Immediate system halt

## Protocol Management

### Creating a New Protocol

1. **Start Protocol Designer**
   ```
   File → New Protocol
   or
   Click "New Protocol" button
   ```

2. **Set Protocol Properties**
   - Protocol name
   - Description
   - Author
   - Version
   - Expected duration

3. **Add Protocol Steps**
   - Aspirate
   - Dispense
   - Mix
   - Wait
   - Move
   - Custom commands

### Protocol Designer Interface

#### Step Library
Pre-defined step types:
- **Aspirate**: Draw liquid into tips
- **Dispense**: Expel liquid from tips
- **Mix**: Aspirate and dispense for mixing
- **Wash**: Clean tips between operations
- **Move**: Reposition without liquid transfer
- **Wait**: Pause for specified time

#### Step Properties
Each step has configurable properties:
```yaml
aspirate_step:
  volume: 100  # μL
  speed: 50    # μL/s
  source: "plate_A1"
  tip_touch: true
  air_gap: 5   # μL
```

#### Visual Editor
- Drag-and-drop step creation
- Real-time protocol validation
- Step reordering and grouping
- Copy/paste functionality

### Protocol Templates

Use predefined templates for common operations:

#### Standard Pipetting Template
```yaml
name: "Standard Pipetting"
steps:
  - type: "aspirate"
    volume: 100
    source: "source_plate"
  - type: "dispense"
    volume: 100
    destination: "destination_plate"
```

#### Serial Dilution Template
```yaml
name: "Serial Dilution 1:2"
steps:
  - type: "aspirate"
    volume: 100
    source: "stock_solution"
  - type: "dispense"
    volume: 50
    destination: "dilution_well_1"
  - type: "mix"
    cycles: 3
    volume: 50
```

## Running Protocols

### Pre-run Checklist

Before running any protocol:
- [ ] Verify device calibration
- [ ] Check tip inventory
- [ ] Confirm reagent volumes
- [ ] Validate protocol steps
- [ ] Clear work area

### Starting a Protocol Run

1. **Load Protocol**
   ```
   Protocols → Open → [Select Protocol]
   ```

2. **Configure Run Parameters**
   - Run name
   - Operator
   - Notes
   - Quality control settings

3. **Verify Setup**
   - Check plate positions
   - Verify tip box placement
   - Confirm reagent containers

4. **Start Execution**
   ```
   Click "Run Protocol" button
   or
   Press F5
   ```

### Monitoring Protocol Execution

#### Real-time Status
- **Progress Bar**: Overall completion percentage
- **Current Step**: Active operation description
- **Estimated Time**: Remaining execution time
- **Volume Tracking**: Aspirated/dispensed volumes

#### Live Log
Monitor execution details:
```
[10:15:23] Protocol started: Serial_Dilution_v1.2
[10:15:24] Aspirating 100 μL from A1
[10:15:26] Dispensing 50 μL to B1
[10:15:28] Mixing 3 cycles in B1
[10:15:32] Step completed successfully
```

### Handling Errors During Execution

#### Common Error Types
- **Volume Error**: Insufficient volume in source
- **Tip Error**: Missing or damaged tips
- **Hardware Error**: Device communication failure
- **Protocol Error**: Invalid step parameters

#### Error Recovery
1. **Review Error Message**: Understand the specific issue
2. **Choose Recovery Option**:
   - Retry step
   - Skip step
   - Abort protocol
   - Manual intervention

3. **Document Resolution**: Add notes to run log

## Data Management

### Viewing Results

#### Results Browser
Access completed runs:
```
Results → Browse Runs
```

Filter and search options:
- Date range
- Protocol name
- Operator
- Run status

#### Result Details
Each run contains:
- **Metadata**: Run parameters and settings
- **Execution Log**: Step-by-step actions
- **Quality Data**: Validation results
- **Files**: Associated data files

### Data Export

#### Export Formats
- **CSV**: Comma-separated values
- **Excel**: XLSX format with formatting
- **JSON**: Machine-readable format
- **PDF**: Formatted report

#### Export Process
1. Select runs to export
2. Choose export format
3. Configure export options
4. Save to desired location

### Data Analysis

#### Built-in Analysis Tools
- **Volume Accuracy**: Compare actual vs. expected volumes
- **Precision Analysis**: Calculate coefficient of variation
- **Trend Analysis**: Performance over time
- **Quality Metrics**: Pass/fail statistics

#### Integration with External Tools
- Export to LIMS systems
- Integration with Excel/R/Python
- API access for custom analysis

## Maintenance

### Daily Maintenance

#### Pre-use Checks
- [ ] Visual inspection of device
- [ ] Check tip inventory
- [ ] Verify reagent levels
- [ ] Test system communication

#### Post-use Procedures
- [ ] Clean liquid pathways
- [ ] Empty waste containers
- [ ] Store tips properly
- [ ] Document any issues

### Weekly Maintenance

- [ ] Volume calibration check
- [ ] Deep clean liquid pathways
- [ ] Replace consumables
- [ ] Backup system data
- [ ] Review maintenance logs

### Monthly Maintenance

- [ ] Full system calibration
- [ ] Update software/firmware
- [ ] Comprehensive cleaning
- [ ] Preventive maintenance
- [ ] Performance validation

### Maintenance Documentation

Record all maintenance activities:
```
Date: 2025-10-04
Operator: John Smith
Activity: Weekly calibration check
Results: All volumes within ±2% tolerance
Notes: Replaced tip box in position 1
Next Due: 2025-10-11
```

## Safety Guidelines

### General Safety

- **Personal Protective Equipment**: Always wear safety glasses and gloves
- **Chemical Handling**: Follow MSDS guidelines for all reagents
- **Emergency Procedures**: Know location of emergency stops and contacts
- **Training Requirements**: Complete training before operation

### System Safety

- **Emergency Stop**: Red button immediately halts all motion
- **Interlock System**: Safety covers must be closed during operation
- **Waste Management**: Proper disposal of contaminated materials
- **Electrical Safety**: Qualified personnel only for electrical work

### Biological Safety

When working with biological materials:
- Use appropriate biosafety level protocols
- Employ proper containment measures
- Follow institutional guidelines
- Document biological waste disposal

## Troubleshooting

### Performance Issues

| Issue | Possible Causes | Solutions |
|-------|----------------|-----------|
| Inaccurate volumes | Calibration drift | Recalibrate system |
| Slow operation | System overload | Reduce concurrent protocols |
| Communication errors | Connection issues | Check cables and drivers |

### User Interface Issues

| Issue | Solution |
|-------|----------|
| Application won't start | Restart Windows service |
| Slow response | Close unnecessary applications |
| Display issues | Update graphics drivers |

### Getting Help

- **Built-in Help**: Press F1 or Help menu
- **Knowledge Base**: Search FAQ and troubleshooting guides
- **Support Ticket**: Submit detailed issue description
- **Phone Support**: For urgent issues

## Appendices

### Appendix A: Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| Ctrl+N | New protocol |
| Ctrl+O | Open protocol |
| Ctrl+S | Save |
| F5 | Run protocol |
| Esc | Stop current operation |
| F12 | Emergency stop |
| F1 | Help |

### Appendix B: System Specifications

- Volume range: 1-1000 μL
- Accuracy: ±1% or ±0.1 μL
- Precision: CV ≤ 1%
- Speed: Up to 200 μL/s
- Channels: 1-8 configurable

### Appendix C: File Formats

- Protocol files: `.hlp` (Haier Liquid Protocol)
- Result files: `.hlr` (Haier Liquid Results)
- Configuration: `.yaml`
- Logs: `.log`

---

*For additional support, contact: support@haier-liquid-handling.com*

*Last updated: October 4, 2025*