Table of Contents
=================

   * [Table of Contents](#table-of-contents)
   * [Purpose](#purpose)
   * [ComfyUI-LLaVA-Captioner](#comfyui-llava-captioner)
      * [ComfyUI Installation](#comfyui-installation)
      * [ComfyUI Running](#comfyui-running)
      * [ComfyUI-LLaVA-Captioner Installation](#comfyui-llava-captioner-installation)
      * [Reference](#reference)
   * [Troubleshooting](#troubleshooting)
   * [Reference](#reference-1)
   * [h1 size](#h1-size)
      * [h2 size](#h2-size)
         * [h3 size](#h3-size)
            * [h4 size](#h4-size)
               * [h5 size](#h5-size)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc)

 
# Purpose
Take note of Multimodal related stuff


# ComfyUI-LLaVA-Captioner  

## ComfyUI Installation  
1. Git clone this repo. 
```bash
git clone https://github.com/comfyanonymous/ComfyUI.git
```

1. Put your SD checkpoints (the huge ckpt/safetensors files) in: ComfyUI\models\checkpoints  
*[ChilloutMix-ni-fp16.safetensors](https://huggingface.co/AnonPerson/ChilloutMix/tree/main)

1. Put your VAE in: ComfyUI\models\vae  
*[vae-ft-mse-840000-ema-pruned.ckpt](https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.ckpt)

1. Dependencies  
```bash
source ~/virtualenv/cuda118_pytorch/bin/activate
pip install -r requirements.txt
```

## ComfyUI Running  
```bash
cd ~/projects/ComfyUI
python main.py
```
*go to: http://localhost:8188*

<img src="images/ComfyUI_01.png" width="800" height="400">  

## ComfyUI Plugins  


### ComfyUI-Manager（插件管理器）：  
[ltdrdata/ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager)

   1. goto ComfyUI/custom_nodes dir in terminal(cmd)
   1. git clone https://github.com/ltdrdata/ComfyUI-Manager.git
   1. Restart ComfyUI

### AIGODLIKE-ComfyUI-Translation（界面汉化）：  
[AIGODLIKE/AIGODLIKE-ComfyUI-Translation](https://github.com/AIGODLIKE/AIGODLIKE-ComfyUI-Translation)

   1. cd ComfyUI/custom_nodes
   1. git clone https://github.com/AIGODLIKE/AIGODLIKE-COMFYUI-TRANSLATION.git

### ComfyUI_Custom_Nodes_AlekPet(提示词中文输入)：  
[AlekPet/ComfyUI_Custom_Nodes_AlekPet](https://github.com/AlekPet/ComfyUI_Custom_Nodes_AlekPet)

   1. Open a terminal or command line interface.
   1. Go to folder ..\ComfyUI\custom_nodes
   1. Enter 
   ```bash
   git clone https://github.com/AlekPet/ComfyUI_Custom_Nodes_AlekPet.git
   ```
   1. After this command be created folder ComfyUI_Custom_Nodes_AlekPet
   1. Run Comflyui....

### sdxl_prompt_styler（SDXL提示词风格预设）：  
[twri/sdxl_prompt_styler](https://github.com/twri/sdxl_prompt_styler)

   1. Open a terminal or command line interface.
   1. Navigate to the ComfyUI/custom_nodes/ directory.
   1. Run the following command: 
   ```bash
   git clone https://github.com/twri/sdxl_prompt_styler.git
   ```
   1. Restart ComfyUI.

### ComfyUI-Custom-Scripts（辅助工具）：  
[pythongosssss/ComfyUI-Custom-Scripts](https://github.com/pythongosssss/ComfyUI-Custom-Scripts)

   1. Open a terminal or command line interface.
   1. Navigate to the ComfyUI/custom_nodes/ directory.
   1. Run the following command: 
   ```bash
   git clone https://github.com/pythongosssss/ComfyUI-Custom-Scripts.git
   ```

### ComfyUI_UltimateSDUpscale (SD放大插件)：  
[ssitu/ComfyUI_UltimateSDUpscale](https://github.com/ssitu/ComfyUI_UltimateSDUpscale)

   1. Enter the following command from the commandline starting in ComfyUI/custom_nodes/  
   ```bash
   git clone https://github.com/ssitu/ComfyUI_UltimateSDUpscale --recursive
   ```

## ComfyUI-LLaVA-Captioner Installation   

1. Dependencies  
```bash
pip install llama-cpp-python
```

2. Download models from 🤗 into models\llama:  
[llava-v1.5-7b-Q4_K.gguf](https://huggingface.co/jartine/llava-v1.5-7B-GGUF/resolve/main/llava-v1.5-7b-Q4_K.gguf)  
[llava-v1.5-7b-mmproj-Q4_0.gguf](https://huggingface.co/jartine/llava-v1.5-7B-GGUF/resolve/main/llava-v1.5-7b-mmproj-Q4_0.gguf)  


## Reference  
[comfyanonymous/ComfyUI](https://github.com/comfyanonymous/ComfyUI?tab=readme-ov-file#installing)  
[【ai绘画】ComfyUI 插件安装](https://www.youtube.com/watch?v=KiLHnRtH2y8)  
[ComfyUI从入门到精通系列-4.升高放大无极限](https://www.youtube.com/watch?v=Bvkt5ZfxTa8&list=PLK7sA3zrSa4s0tO8w2pdc7zPTcIAgS7ru&index=4)  


ComfyUI LLaVA Captioner  
[ceruleandeep/ComfyUI-LLaVA-Captioner](https://github.com/ceruleandeep/ComfyUI-LLaVA-Captioner)  
[pythongosssss/ComfyUI-WD14-Tagger](https://github.com/pythongosssss/ComfyUI-WD14-Tagger)    

[WindowsPC に Stable Diffusion ComfyUI をインストールする方法 2023-10-27](https://qiita.com/zono_0/items/ea370c24a34284e07d03)  
[ComfyUIで生成したpngから、WorkFlowを復元するPythonコードをGPT4の手助けで即席に作れたよ 2023-08-16](https://qiita.com/quittardis/items/781386c1072938ddeed1)  
[WindowsPC に StabilityMatrix をインストールする方法 2023-10-28](https://qiita.com/zono_0/items/1638d9075497cf105512)  
[ComfyUIをApple M1で試してみる 2024-01-09](https://qiita.com/TaitoOtani/items/be2298582e8e0b5d1a32)  
[RadeonでkritaAIを動かす備忘録 2024-02-19](https://qiita.com/hikisari/items/bae429cd530606324041)


# Troubleshooting


# Reference
MMC: Advancing Multimodal Chart Understanding with LLM Instruction Tuning  
[FuxiaoLiu/MMC ](https://github.com/FuxiaoLiu/MMC?tab=readme-ov-file)


tstock - Generate stock charts in the terminal!  
[ Gbox4/tstock](https://github.com/Gbox4/tstock)



XTuner is an efficient, flexible and full-featured toolkit for fine-tuning large models.  
[InternLM /xtuner](https://github.com/InternLM/xtuner)


Stock-Market-Predcition-using-ResNet  
[ jason887/Using-Deep-Learning-Neural-Networks-and-Candlestick-Chart-Representation-to-Predict-Stock-Market](https://github.com/jason887/Using-Deep-Learning-Neural-Networks-and-Candlestick-Chart-Representation-to-Predict-Stock-Market)

Running a Multimodal LLM locally with Ollama and LLaVA Feb 3, 2024](https://www.jeremymorgan.com/blog/generative-ai/how-to-multimodal-llm-local/)
[Run Open Source Multimodal Models Locally Using Ollama Feb 4, 2024](https://medium.com/@sudarshan-koirala/run-open-source-multimodal-models-locally-using-ollama-24cb1bb8b955)

[日本語LLMでLLaVAの学習を行ってみた 2023-12-24](https://qiita.com/toshi_456/items/248005a842725f9406e3)  
[tosiyuki/LLaVA-JP](https://github.com/tosiyuki/LLaVA-JP/tree/main)
[LLaVA 2023-11-14](https://qiita.com/fuyu_quant/items/2692198b65d9763b45a2)
[haotian-liu/LLaVA](https://github.com/haotian-liu/LLaVA)  
[LLaVA: The Open-Source Multimodal Model That's Changing the Game 12/17/2023](https://cheatsheet.md/llm-leaderboard/LLaVA)
[LLaVA: An open-source alternative to GPT-4V(ision) Jan 24, 2024](https://towardsdatascience.com/llava-an-open-source-alternative-to-gpt-4v-ision-b06f88ce8efa)
[Vision models](https://ollama.com/blog/vision-models)

[PKU-YuanGroup/Video-LLaVA](https://github.com/PKU-YuanGroup/Video-LLaVA)

* []()  
![alt tag]()
<img src="" width="400" height="500">  

# h1 size

## h2 size

### h3 size

#### h4 size

##### h5 size

*strong*strong  
**strong**strong  

> quote  
> quote

- [ ] checklist1
- [x] checklist2

* 1
* 2
* 3

- 1
- 2
- 3

No. | Test Name 
------------------------------------ | --------------------------------------------- | 
001 | Two Sum
