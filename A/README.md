---
marp: true
theme: default
header: 기계학습 A형 과제 PPT
footer: 20211343 소프트웨어학과 김동현
paginate: true
---

<head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.15.6/styles/default.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.15.6/highlight.min.js"></script>
    <script>hljs.initHighlightingOnLoad();</script>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/purecss@3.0.0/build/pure-min.css" integrity="sha384-X38yfunGUhNzHpBaEBsWLO+A0HDYOQi8ufWDkZ0k9e0eXz/tH3II7uKZ9msv++Ls" crossorigin="anonymous">
</head>

<h2>
Generative Adversarial Network를 통한 <br />
글자 단위로 타임스탬프를 찍을 수 있는 AI 모델
</h2>

<p>
키워드: Generative Adversarial Network, Text-To-Sound, Sound-To-Text
</p>

---

## 연구의 필요성

1. 개인적인 목적
2. 연구적인 목적

---

## 연구의 필요성: 개인적인 목적

<div class="pure-g">
    <div class="pure-u-3-4">
        <ol style="font-size: 1.375rem">
            <li>
                개인적으로 이전에 노래방 UI를 웹사이트에서 구현하는 프로젝트를 진행했습니다.
            </li>
            <li>
                단, 이 프로젝트는 "완성된 MIDI 파일, 음원 파일이 필요하기 때문에 개인의 접근성이 떨어진다"는 단점이 있었습니다.
            </li>
            <li>
                <i>YouTube</i>에서 음원을 가져와 노래방 기능을 구현하는 프로젝트를 기획했는데, 오른쪽 사진과 같이 노래방 자막을 구현하려면 <strong>'글자 단위' 타임스탬프가 있는 자막 데이터</strong>가 필요합니다.
            </li>
        </ol>
    </div>
    <div class="pure-u-1-4" style="text-align: center;">
        <img src="./assets/lyric-sample.png" />
    </div>
</div>

---

## 연구의 필요성: 연구적인 목적

<ol style="font-size: 1.25rem">
  <li>
    현재 거대 AI 기업들은 다양한 Text-To-Speech 및 Speech-To-Text 모델을 개발하고 있습니다.
  </li>
  <li>
    Speech-To-Text 모델은 일반적으로 '단어 단위' 타임스탬프를 지원합니다. 다만 '글자 단위' 타임스탬프를 지원하는 모델은 극소수입니다.
  </li>
  <li>
    극소수에 해당하는 모델인 VOSK, ESPNet의 경우 
  </li>
  <li>
    본 연구에서는 현존하는 음원, 가사 데이터와 TTS 모델을 통한 가상 데이터를 사용하여 글자 단위로 타임스탬프를 도출할 수 있는 Speech-To-Text 모델을 개발하고자 합니다.
  </li>
</ol>

---

## 연구의 필요성: 정리

<div class="pure-g">
    <div class="pure-u-1-2">
        <h3>개인적으로</h3>
        <span>원하는 프로젝트를 개발하기 위해서 필요한 선수과제</span>
    </div>
    <div class="pure-u-1-2">
        <h3>연구적으로</h3>
        <span>글자 단위까지 타임스탬프를 얻어낼 수 있는 새로운/개선된 모델 개발</span>
    </div>
</div>

---

## 관련 연구

---

## 연구 방법

<ol style="font-size: 1.25rem">
  <li>
    <strong>학습 데이터 구하기: </strong>
    크롤링 및 외부 API를 통해 인기 있는 음원 및 가사를 다운로드하고, TTS 모델을 통해 가상 데이터를 생성합니다.
  </li>
  <li>
    <strong>학습하기: </strong>
    이미 존재하는 음원 파일과 가상 데이터를 통해 학습시킵니다 (음원 파일과 생성된 데이터를 모두 사용하는 것은 편향성 감소를 위함입니다)
  </li>
  <li>
    <strong>평가하기: </strong>
    학습이 모두 끝났다면 '가사를 정확하게 인식했는가', '글자 타임스탬프가 정확하게 도출되었는가'를 기준으로 하여 결과를 평가합니다.
  </li>
  <li>
    <strong>반복하기: </strong>
    이후 모델의 인식률, 글자 타임스탬프 예측 정확도 향상을 위해 학습을 반복합니다.
  </li>
</ol>

---

## 예상되는 결과

<div class="pure-g">
    <div class="pure-u-10-24">
        <strong>Standard STT</strong>
    </div>
    <div class="pure-u-1-6"></div>
    <div class="pure-u-10-24">
        <strong>letter-scale STT</strong>
    </div>
    <div class="pure-u-10-24">
        <pre class="json" data-ke-type="codeblock" style="font-size: 1rem;">
            <code>
[
    {
        "단어": "동해물과",
        "시작": 0,
        "끝": 1000
    }
]
            </code>
        </pre>
        <div style="font-size: 1.25rem;">
            다른 STT 모델과 달리 <strong>글자 단위의 타임스탬프</strong>를 얻을 수 있으면서, <br />
            다른 STT 모델과 <strong>비슷하거나, 더 나은 인식률</strong>을 가지는 모델의 개발
        </div>
    </div>
    <div class="pure-u-1-6">
        <center>
            &rarr;
        </center>
    </div>
    <div class="pure-u-10-24">
        <pre class="json" data-ke-type="codeblock" style="font-size: 1rem;">
            <code>
[
    {
        "자": "동",
        "시작": 0,
        "끝": 200
    },
    {
        "자": "해",
        "시작": 300,
        "끝": 500
    },
    {
        "자": "물",
        "시작": 700,
        "끝": 900
    },
    {
        "자": "과",
        "시작": 1000,
        "끝": 1200
    }
]
            </code>
        </pre>
    </div>
</div>

<!-- 연구자는 현재까지 관련 연구를 한 경험이 전무하기 때문에 매우 낮은 정확도 및 느린 성능을 가진 모델이 개발될 것이라 생각합니다.
하지만 본 연구는 연구적인 목적과 함께 개인적인 목적도 함께 갖춘 아이디어이기에 개인적으로 모델의 구조를 수정하고, 데이터를 개선 및 다양화하는 등 꾸준히 모델을 개선하고자 합니다. -->

---

## 참고 문헌

- [VOSK; Vosk Speech Recognition Toolkit, https://github.com/alphacep/vosk-api](https://github.com/alphacep/vosk-api)
- [ESPNet https://github.com/espnet/espnet](https://github.com/espnet/espnet)
- [VOSK Versus Coqui STT - A practical comparison.](https://github.com/alphacep/vosk-api/issues/892)
- [Momentum Pseudo-Labeling for Semi-Supervised Speech Recognition; Yosuke Higuchi](https://arxiv.org/pdf/2106.08922.pdf)
- [ESPnet: End-to-End Speech Processing Toolkit; Shinji Watanabe, Takaaki Hori, Shigeki Karita, Tomoki Hayashi, Jiro Nishitoba, Yuya Unno, Nelson Enrique Yalta Soplin, Jahn Heymann, Matthew Wiesner, Nanxin Chen, Adithya Renduchintala, Tsubasa Ochiai](https://arxiv.org/pdf/1804.00015.pdf)
