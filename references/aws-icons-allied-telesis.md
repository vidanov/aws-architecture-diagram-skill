# Icons: Allied Telesis isometric computer/server/network (bonus library for 3D diagrams)

Companion to `aws-icons-3d.md`. Use this when a **3D/isometric** diagram needs a generic client device, on-prem server, server rack, or network hardware icon that has no AWS-specific equivalent in `mxgraph.aws3d.*`. Verified directly against draw.io's own source: `https://raw.githubusercontent.com/jgraph/drawio/master/src/main/webapp/js/diagramly/sidebar/Sidebar-AlliedTelesis.js`.

## Critical facts

- Unlike `aws3d`/`aws4`, these are **not stencil shapes** — they are SVG **images** bundled inside the draw.io app itself, referenced by relative path. Style pattern:
  ```
  image;points=[];aspect=fixed;html=1;align=center;shadow=0;dashed=0;image=img/lib/allied_telesis/<category>/<File>.svg;
  ```
- Because the image path is relative to draw.io's own bundled assets, this only renders correctly when the `.drawio` file is opened inside an actual draw.io instance (diagrams.net web app, desktop app, or VS Code extension) — which is the normal way these files get opened, so this is not a practical limitation, just something to be aware of if ever rendering outside draw.io.
- Only use these for generic hardware that has no AWS-specific icon. Don't substitute them for an AWS service that already has a real icon in `aws3d` (e.g. don't swap out `dynamoDb` or `lambda`) — mixing in generic hardware icons only where AWS has no equivalent keeps the diagram coherent.

## Verified shape table (sizes are w x h in px)

### `computer_and_terminals/` — clients, on-prem servers, terminals
| File | Display Name | Size |
|---|---|---|
| `Personal_Computer.svg` | Personal Computer | 46 x 62 |
| `Personal_Computer_Wireless.svg` | Personal Computer (Wireless) | 63 x 64 |
| `Personal_Computer_with_Server.svg` | Personal Computer with Server | 62 x 62 |
| `Laptop.svg` | Laptop | 42 x 43 |
| `Server_Desktop.svg` | Server (Desktop form factor) | 43 x 54 |
| `Smartphone.svg` | Smartphone | 20 x 43 |
| `Tablet.svg` | Tablet | 27 x 57 |
| `Tablet_Alternative.svg` | Tablet (alt) | 35 x 48 |
| `IP_TV.svg` | IP TV | 49 x 50 |
| `Keypad.svg` | Keypad | 26 x 48 |
| `POS_keypad.svg` | POS Keypad | 37 x 28 |
| `POS_Printer.svg` | POS Printer | 37 x 32 |
| `Vdeo_Conference_Terminal.svg` | Video Conference Terminal | 32 x 45 |
| `VOIP_IP_phone.svg` | VOIP IP Phone | 30 x 46 |

### `storage/` — server racks / datacenter compute
| File | Display Name | Size |
|---|---|---|
| `Datacenter_Server_Rack.svg` | Datacenter Server Rack | 88 x 179 |
| `Datacenter_Server_Rack_ToR.svg` | Datacenter Server Rack (Top of Rack) | 88 x 179 |
| `Datacenter_Server_Rack_EoR.svg` | Datacenter Server Rack (End of Row) | 86 x 173 |
| `Datacenter_Server_Half_Rack_ToR.svg` | Half Rack (ToR) | 88 x 115 |
| `Datacenter_Server_Rack_Storage_Unit_Small.svg` | Small Storage Unit | 77 x 67 |
| `Datacenter_Server_Storage_Unit_Large.svg` | Large Storage Unit | 77 x 79 |

### `switch/` — network switches
| File | Display Name | Size |
|---|---|---|
| `Switch_24_port_L2.svg` | 24-port L2 switch | 74 x 51 |
| `Switch_24_port_L2_POE.svg` | 24-port L2 POE switch | 74 x 51 |
| `Switch_24_port_L3.svg` | 24-port L3 switch | 74 x 51 |
| `Switch_24_port_L3_POE.svg` | 24-port L3 POE switch | 74 x 51 |
| `Switch_48_port_L2.svg` | 48-port L2 switch | 78 x 53 |
| `Switch_48_port_L2_POE.svg` | 48-port L2 POE switch | 78 x 53 |
| `Switch_48_port_L3.svg` | 48-port L3 switch | 78 x 53 |
| `Switch_48_port_L3_POE.svg` | 48-port L3 POE switch | 78 x 53 |
| `Switch_52_port_L3.svg` | 52-port L3 switch | 78 x 53 |
| `Modular_Switch_SBx8106.svg` | Modular chassis switch | 86 x 74 |
| `Modular_Switch_SBx8112.svg` | Modular chassis switch | 89 x 92 |
| `Modular_Switch_SXx908GEN2.svg` | Modular chassis switch | 78 x 67 |
| `Industrial_Ethernet_IE200.svg` | Industrial switch | 40 x 56 |
| `Industrial_Ethernet_IE200_POE.svg` | Industrial switch (POE) | 40 x 56 |
| `Industrial_Ethernet_IE300.svg` | Industrial switch | 70 x 77 |

### `wireless/`
| File | Display Name | Size |
|---|---|---|
| `Access_Point_Indoor.svg` | Indoor Access Point | 37 x 55 |
| `Access_Point_Outdoor.svg` | Outdoor Access Point | 26 x 100 |
| `Laptop_Wireless.svg` | Laptop (Wireless) | 58 x 47 |

### `security/`
| File | Display Name | Size |
|---|---|---|
| `Router_UTM.svg` | Router (UTM) | 56 x 40 |
| `Router_VPN.svg` | Router (VPN) | 56 x 40 |
| `POS.svg` | POS Terminal | 68 x 72 |
| `EtherGRID.svg` | EtherGRID | 89 x 65 |
| `POE_DVS_Camera.svg` | POE DVS Camera | 51 x 40 |
| `DVS_Surveillance_Monitor.svg` | DVS Surveillance Monitor | 42 x 60 |
| `Surveillance_Camera_Ceiling.svg` | Ceiling Surveillance Camera | 37 x 35 |

### `media_converters/`
| File | Display Name | Size |
|---|---|---|
| `Media_Converter_Standalone.svg` | Media Converter (Standalone) | 46 x 37 |
| `Media_Converter_Standalone_POE.svg` | Media Converter (Standalone, POE) | 46 x 37 |
| `Media_Converter_Modular.svg` | Media Converter (Modular) | 71 x 55 |
| `Industrial_Media_Converter.svg` | Industrial Media Converter | 30 x 57 |
| `Industrial_Media_Converter_POE.svg` | Industrial Media Converter (POE) | 30 x 57 |

### `buildings/`
Offices, apartments, campuses — rarely relevant to a service architecture diagram. See the source file if ever needed.

## When to use these vs. `aws3d`

Reach for Allied Telesis icons for: generic client devices (nicer than `aws3d.client` for a plain "user's computer" node), on-prem/EC2-style servers, server racks/datacenters, and any network hardware (switches, APs, routers) — none of which has a real icon in either AWS icon library. Keep using `aws3d` for anything that's an actual named AWS service.

## Source of truth
`https://raw.githubusercontent.com/jgraph/drawio/master/src/main/webapp/js/diagramly/sidebar/Sidebar-AlliedTelesis.js` — re-fetch and grep this directly for anything not covered above rather than guessing.
