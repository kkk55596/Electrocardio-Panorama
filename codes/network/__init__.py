from .model_v9 import ModelV9
from torch.nn import MSELoss, L1Loss, CrossEntropyLoss

from .loss import losswrapper, MSELead


def build_model(cfg):
    model_name = cfg.MODEL.model
    if model_name == 'modelv9':
        return ModelV9(theta_encoder_len=cfg.MODEL.theta_L, lead_num=cfg.DATA.lead_num)
    else:
        raise ValueError('build model: model name error')


def build_loss(cfg):
    loss_name = cfg.MODEL.loss
    if loss_name == 'v1':
        return losswrapper
    elif loss_name == 'ce':
        return CrossEntropyLoss()
    elif loss_name == 'mse':
        return MSELoss()
    else:
        raise ValueError('build loss: loss name error')

