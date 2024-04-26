.. learning_transformer documentation master file, created by
   sphinx-quickstart on Tue Mar 26 09:39:22 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to learning_transformer's documentation!
================================================

- **Author:** Colin
- **Mail:** xranger@qq.com
- **Github:** https://www.github.com/jmge/leanring_transformer


卷积神经网络（Convolutional Neural Networks，CNN）和Transformer是两种在深度学习中广泛应用的架构，分别用于处理视觉和自然语言等不同类型的数据。以下是它们之间的技术比较：

1. **结构差异**：
   #. CNN：CNN主要由卷积层和池化层组成。卷积层通过卷积操作提取输入图像的特征，池化层则用于减小特征图的空间尺寸，减少计算量。
   #. Transformer：Transformer是一种基于自注意力机制的模型，主要由自注意力层和前馈神经网络层组成。自注意力层用于捕捉序列中不同位置之间的依赖关系，前馈神经网络层则用于处理每个位置的特征。

2. **适用领域**：
   #. CNN：CNN主要用于处理图像数据，例如图像分类、目标检测和图像分割等任务。
   #. Transformer：Transformer最初用于处理自然语言数据，如机器翻译、文本生成和语言模型等任务，但也被应用于其他序列数据的任务，如音频处理和时间序列分析等。

3. **处理序列长度**：
   - CNN：CNN对于输入数据的尺寸不敏感，但在处理长序列数据时可能存在限制，需要通过调整网络结构或使用循环机制（如LSTM或GRU）来处理。
   - Transformer：Transformer能够直接处理变长序列数据，并且在处理长序列数据时具有较好的表现，但在序列长度增加时，也需要更多的计算资源。

4. **平行化**：
   - CNN：CNN中的卷积操作可以并行计算，因此在硬件上具有较好的可扩展性。
   - Transformer：传统的Transformer模型中，自注意力机制会导致序列中每个位置的计算都依赖于其它位置，难以进行有效的并行计算。但通过一些技术改进（如多头注意力），可以提高Transformer的并行性。

5. **全局信息处理**：
   - CNN：在CNN中，每个位置的输出只受到局部区域的输入影响，因此在捕获全局信息方面可能存在局限性。
   - Transformer：Transformer通过自注意力机制可以捕获输入序列的全局信息，因此在处理长距离依赖关系时表现更好。

6. **参数量和训练速度**：
   - CNN：CNN通常具有较少的参数量，可以更容易地训练，尤其是对于小型数据集。
   - Transformer：传统的Transformer模型通常具有较大的参数量，需要更多的数据和计算资源来进行训练。

总的来说，CNN和Transformer是两种不同的深度学习架构，各自在处理不同类型的数据和任务时具有各自的优势和局限性。


.. code-block:: console
	:caption: this is code caption
	:linenos:
	:emphasize-lines: 1
	
	pip install lumache
	this is a code block.
	code1
	cod2

.. code-block:: console
   :caption: testcodeblock
   :linenos:

   this is the first line of test code
   this is the second line of test code
   this is the third line of test code
   this is the fourth line of test code



.. _Contents:

.. toctree:: 
   :maxdepth: 3
   :numbered:
   :caption: 目录

   embed
   intro
   transf
   test
   xx

	



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
