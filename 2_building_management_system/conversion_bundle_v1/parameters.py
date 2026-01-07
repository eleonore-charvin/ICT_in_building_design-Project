
import numpy as np

parameter = {}
parameter['seed']       = 1
parameter['store_data'] = True

dtype = np.float64
parameter['fmu_step_size']   = 3600 / 6
parameter['fmu_path']        = 'ResFlatdue_IDF_EMS_optimal.fmu'
parameter['fmu_start_time']  = 0 * 60 * 60 * 24
parameter['fmu_warmup_time'] = 3 * 60 * 60 * 24
parameter['fmu_final_time']  = 24 * 60 * 60 * 24

parameter['action_names']      = ['Zona4_wall2_shade_FMU', 'Zona2_wall2_shade_FMU', 'Zona2_wall3_shade_FMU', 'Zona1_wall2_shade_FMU', 'Zona1_wall8_shade_FMU', 'Zona1_wall9_shade_FMU', 'HeatSP_cmd_z1', 'HeatSP_cmd_z2', 'HeatSP_cmd_z3', 'HeatSP_cmd_z4', 'CoolSP_cmd_z1', 'CoolSP_cmd_z2', 'CoolSP_cmd_z3', 'CoolSP_cmd_z4']
parameter['action_min']        = np.array([-1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000, -1000], dtype=np.float64)
parameter['action_max']        = np.array([1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000], dtype=np.float64)
parameter['observation_names'] = ['Tair_z1', 'Tair_z2', 'Tair_z3', 'Tair_z4', 'H_unmet_z1', 'C_unmet_z1', 'T_ext', 'DNI', 'DistrictHeating', 'DistrictCooling', 'Electricity', 'ShadeStatus_Zone1_Wall2', 'ShadeStatus_Zone1_Wall8', 'ShadeStatus_Zone1_Wall9', 'ShadeStatus_Zone2_Wall2', 'ShadeStatus_Zone2_wall3', 'ShadeStatus_Zone4_Wall2', 'HeatSP_z1', 'HeatSP_z2', 'HeatSP_z3', 'HeatSP_z4', 'CoolSP_z1', 'CoolSP_z2', 'CoolSP_z3', 'CoolSP_z4', 'HeatingEnergy_z1', 'HeatingEnergy_z2', 'HeatingEnergy_z3', 'HeatingEnergy_z4', 'CoolingEnergy_z1', 'CoolingEnergy_z2', 'CoolingEnergy_z3', 'CoolingEnergy_z4']
parameter['reward_names']      = []

