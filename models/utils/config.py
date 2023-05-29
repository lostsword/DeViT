model_config = {
    'dedeit': {'patch_size': 16, 'embed_dim': 192, 'depth': 12, 'num_heads': 3,
                              'mlp_ratio': 4, 'qkv_bias': True,
                              'norm_layer': partial(nn.LayerNorm, eps=1e-6)},
    'deit_base_distilled_patch16_224': {'patch_size': 16, 'embed_dim': 768, 'depth': 12, 'num_heads': 12,
                              'mlp_ratio': 4, 'qkv_bias': True,
                              'norm_layer': partial(nn.LayerNorm, eps=1e-6)},
    'vit_large_patch16_224': {'patch_size': 16, 'embed_dim': 1024, 'depth': 24, 'num_heads': 16,
                              'mlp_ratio': 4, 'qkv_bias': True,
                              'norm_layer': partial(nn.LayerNorm, eps=1e-6)},
    'vit_base_patch16_224': {'patch_size': 16, 'embed_dim': 768, 'depth': 12, 'num_heads': 12,
                             'mlp_ratio': 4, 'qkv_bias': True,
                             'norm_layer': partial(nn.LayerNorm, eps=1e-6)},
    'devit': {'patch_size': 16, 'embed_dim': 192, 'depth': 12, 'num_heads': 3,
                             'mlp_ratio': 4, 'qkv_bias': True,
                             'norm_layer': partial(nn.LayerNorm, eps=1e-6)},
}