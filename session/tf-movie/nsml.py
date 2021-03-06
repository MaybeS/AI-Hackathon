HAS_DATASET = False
IS_ON_NSML = False
DATASET_PATH = '../../sample_data/movie_review'
GPU_NUM = 0

_save = lambda x: None
_load = lambda x: None
_infer = lambda x: None 

def paused(scope):
    pass

def save(*args, **kwargs):
    global _save
    return _save('./tmp', *args, **kwargs)

def load(*args, **kwargs):
    global _load
    return _load('./tmp', *args, **kwargs)

def infer(*args, **kwargs):
    global _infer
    return _infer(*args, **kwargs)

def report(summary, scope, epoch, total_epoch, val_acc, train_acc, train__loss, val__loss, step):
    pass

def bind(save, load, infer):
    global _save, _load, _infer
    _save = save
    _load = load
    _infer = infer
